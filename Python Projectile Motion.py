import matplotlib.pyplot as plt
import numpy as np
import math


pvx, px = [], []
pt, pvy, py = [], [], []


#   ================================================    set your parameters here    ================================================
v0 = 2.2        # initial velocity in meters per second
angle = 15.0    # launch angle in degrees
x0 = 0.0        # initial X position in meters (usually 0)
y0 = 0.41       # initial Y position in meters
g = -9.81       # acceleration due to gravity in meters per second squared
ar = 0        # air resistance (0 if neglecting air resistance)
dt = 0.05       # time increment in seconds


#   ======================================    initial conditions for computation variables    ======================================
vx0 = v0 * math.cos(math.radians(angle))    # initial x velocity in miles per hour
vy0 = v0 * math.sin(math.radians(angle))    # initial y velocity in miles per hour
y = y0
x = x0
v = v0
vx = vx0
vy = vy0
t = 0

#   ==================================================    compute Vy, Vx, Y, X    ==================================================
#   ==========================================    loop until projectile hits the ground    =========================================
while y >= 0:
#   =========================================   append values into array for graphs below    =======================================
    pt.append(t)
    pvx.append(vx)
    px.append(x)
    pvy.append(vy)
    py.append(y)


#   ========================================    compute position and velocity components    ========================================
    t = t + dt                              # increment time by delta time
    x = x + (vx * dt)                       # new x position = old x position +  x velocity * distance
    y = y + (vy * dt)                       # new y position = old y position +  y velocity * distance
    vx = vx - (ar * vx * dt)                # new x velocity = old x velocity - air resistance
    vy = vy + (g * dt) - (ar * vy * dt)     # new y velocity = old y velocity + gravity - air resistance
    
#v = math.sqrt(vx ** 2 + vy ** 2)   === commented because this line of code was unused anywhere else ===    new velocity= square root of x velocity ** 2 + y velocity ** 2


#   ====================================================    create the plots    ====================================================
fig = plt.figure(figsize=(22,14))
grid = plt.GridSpec(2, 2, wspace=0.25, hspace=0.25)
ax1 = plt.subplot(grid[0,0])
ax2 = plt.subplot(grid[0,1])
ax3 = plt.subplot(grid[1,:])

# vy(t)
color = 'tab:red'
ax1.set_xlabel('time (s)', fontsize=16)
ax1.set_ylabel('Vy (m/s)', color=color, fontsize=16)
ax1.tick_params(axis='y', labelcolor=color, labelsize=14)
ax1.tick_params(axis='x', labelsize=14)
ax1.plot(pt, pvy, '.-', color=color)
ax1.grid(which='both', axis='both', alpha=.4,linestyle='--')

# y(t)
color = 'tab:blue'
ax1b = ax1.twinx()
ax1b.set_ylabel('Y (m)', color=color, fontsize=16)
ax1b.tick_params(axis='y', labelcolor=color, labelsize=14)
ax1b.plot(pt, py, '+-', color=color)
ax1b.grid(which='both', axis='both', alpha=.4,linestyle='--')
ax1.set_title('Vy(t) and Y(t)', fontsize=16)

# vx(t)
color = 'tab:red'
ax2.set_xlabel('time (s)', fontsize=16)
ax2.set_ylabel('Vx (m/s)', color=color, fontsize=16)
ax2.tick_params(axis='y', labelcolor=color, labelsize=14)
ax2.tick_params(axis='x', labelsize=14)
ax2.plot(pt, pvx, '.-', color=color)
ax2.grid(which='both', axis='both', alpha=.4,linestyle='--')
ax2.set_title('Vx(t) and X(t)', fontsize=16)

# x(t)
color = 'tab:blue'
ax2b = ax2.twinx()
ax2b.set_ylabel('X (m)', color=color, fontsize=16)
ax2b.tick_params(axis='y', labelcolor=color, labelsize=14)
ax2b.plot(pt, px, '+-', color=color)
ax2b.grid(which='both', axis='both', alpha=.4,linestyle='--')

# y vs x plot
color = 'tab:brown'
ax3.set_xlabel('X (m)', fontsize=16)
ax3.set_ylabel('Y (m)', color=color, fontsize=16)
ax3.tick_params(axis='y', labelcolor=color, labelsize=14)
ax3.tick_params(axis='x', labelsize=14)
ax3.plot(px, py, '.-', color=color)
ax3.grid(which='both', axis='both', alpha=.4,linestyle='--')
ax3.set_title('Y(t) vs X(t)', fontsize=16)

#fig.tight_layout(pad=0.05)  # otherwise the right y-label is slightly clipped

plt.show()