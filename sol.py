import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity

d=pd.read_csv("C:/Users/saanv/Downloads/aasgn2/data.csv",encoding="latin1",low_memory=False)
d.columns=d.columns.str.strip()
x=d["no2"].dropna().values

roll=102483080
a=0.5*(roll%7)
b=0.3*((roll%5)+1)

z=x+a*np.sin(b*x)
z=z.reshape(-1,1)
z=torch.tensor(z,dtype=torch.float32)

class Gnet(nn.Module):
    def __init__(self):
        super().__init__()
        self.m=nn.Sequential(nn.Linear(1,32),nn.ReLU(),nn.Linear(32,32),nn.ReLU(),nn.Linear(32,1))
    def forward(self,x):
        return self.m(x)

class Dnet(nn.Module):
    def __init__(self):
        super().__init__()
        self.m=nn.Sequential(nn.Linear(1,32),nn.ReLU(),nn.Linear(32,32),nn.ReLU(),nn.Linear(32,1),nn.Sigmoid())
    def forward(self,x):
        return self.m(x)

G=Gnet()
D=Dnet()
lossf=nn.BCELoss()
go=optim.Adam(G.parameters(),lr=0.001)
do=optim.Adam(D.parameters(),lr=0.001)

epochs=2000
bs=64

for e in range(epochs):
    idx=np.random.randint(0,len(z),bs)
    real=z[idx]
    noise=torch.randn(bs,1)
    fake=G(noise)

    D.zero_grad()
    rl=torch.ones(bs,1)
    fl=torch.zeros(bs,1)
    rl_loss=lossf(D(real),rl)
    fl_loss=lossf(D(fake.detach()),fl)
    dl=rl_loss+fl_loss
    dl.backward()
    do.step()

    G.zero_grad()
    gl=lossf(D(fake),rl)
    gl.backward()
    go.step()

noise=torch.randn(5000,1)
gen=G(noise).detach().numpy()

kde=KernelDensity(kernel='gaussian',bandwidth=1.0)
kde.fit(gen)

zr=np.linspace(z.min().item(),z.max().item(),500).reshape(-1,1)
ld=kde.score_samples(zr)
dens=np.exp(ld)

plt.hist(z.numpy(),bins=50,density=True,alpha=0.5,label="Real Data")
plt.plot(zr,dens,label="GAN Estimated PDF")
plt.legend()
plt.title("GAN Learned Probability Density Function")
plt.xlabel("z")
plt.ylabel("Density")
plt.savefig("gan_pdf_plot.png",dpi=300)
plt.show()

print("a_r =",a)
print("b_r =",b)
