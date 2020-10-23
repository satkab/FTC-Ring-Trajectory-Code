import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.widgets import Slider, Button


pvx, px = [], []
pt, pvy, py = [], [], []


#   ================================================    set your parameters here    ================================================
v0 = 300            # initial velocity in inches per second
angle = 15.0        # launch angle in degrees
x0 = 0.0            # initial X position in inches (usually 0)
y0 = 16             # initial Y position in inches
g = -386.220472     # acceleration due to gravity in inches per second squared
ar = 0              # air resistance (0 if neglecting air resistance)
dt = 0.02           # time increment in seconds


#   this function is called initially and when the parameters are changed
def compute():
    pt.clear()
    pvy.clear()
    py.clear()
    pvx.clear()
    px.clear()


#   initial conditions for computation variables
vx0 = v0 * math.cos(math.radians(angle))    # initial x velocity
vy0 = v0 * math.sin(math.radians(angle))    # initial y velocity
y = y0
x = x0
v = v0
vx = vx0
vy = vy0
t = 0


#   compute vy, vx, y, x
#   loop until projectile hits the ground
while y >= 0:
#   append values into array for graphs below
    pt.append(t)
    pvx.append(vx)
    px.append(x)
    pvy.append(vy)
    py.append(y)

#   compute position and velocity components
    t = t + dt                              # increment time by delta time
    x = x + (vx * dt)                       # new x position = old x position +  x velocity * distance
    y = y + (vy * dt)                       # new y position = old y position +  y velocity * distance
    vx = vx - (ar * vx * dt)                # new x velocity = old x velocity - air resistance
    vy = vy + (g * dt) - (ar * vy * dt)     # new y velocity = old y velocity + gravity - air resistance


#   call compute() initially to scale graphs below
compute()

# Create the plots
fontsize = 12
labelsize = 12

fig = plt.figure(figsize=(9,5))
grid = plt.GridSpec(2, 2, wspace=0.35, hspace=0.35)
ax1 = plt.subplot(grid[0,0])
ax2 = plt.subplot(grid[0,1])
ax3 = plt.subplot(grid[1,:])

# vy(t)
color = 'tab:red'
ax1.set_xlabel('time (s)', fontsize=fontsize)
ax1.set_ylabel('vy (in/s)', color=color, fontsize=fontsize)
ax1.tick_params(axis='y', labelcolor=color, labelsize=labelsize)
ax1.tick_params(axis='x', labelsize=labelsize)
line1, = ax1.plot(pt, pvy, '.-', color=color)
ax1.grid(which='both', axis='both', alpha=.4, linestyle='--')

# y(t)
color = 'tab:blue'
ax1b = ax1.twinx()
ax1b.set_ylabel('y (in)', color=color, fontsize=fontsize)
ax1b.tick_params(axis='y', labelcolor=color, labelsize=labelsize)
line1b, = ax1b.plot(pt, py, '.-', color=color)
ax1b.grid(which='both', axis='both', alpha=.4,linestyle='--')
ax1.set_title('vy(t) and y(t)', fontsize=fontsize)

# vx(t)
color = 'tab:red'
ax2.set_xlabel('time (s)', fontsize=fontsize)
ax2.set_ylabel('vx (in/s)', color=color, fontsize=fontsize)
ax2.tick_params(axis='y', labelcolor=color, labelsize=labelsize)
ax2.tick_params(axis='x', labelsize=labelsize)
line2, = ax2.plot(pt, pvx, '.-', color=color)
ax2.grid(which='both', axis='both', alpha=.4,linestyle='--')
ax2.set_title('vx(t) and x(t)', fontsize=fontsize)

# x(t)
color = 'tab:blue'
ax2b = ax2.twinx()
ax2b.set_ylabel('x (in)', color=color, fontsize=fontsize)
ax2b.tick_params(axis='y', labelcolor=color, labelsize=labelsize)
line2b, = ax2b.plot(pt, px, '.-', color=color)
ax2b.grid(which='both', axis='both', alpha=.4,linestyle='--')

# y vs x plot
color = 'tab:brown'
ax3.set_xlabel('x (in)', fontsize=fontsize)
ax3.set_ylabel('y (in)', color=color, fontsize=fontsize)
ax3.tick_params(axis='y', labelcolor=color, labelsize=labelsize)
ax3.tick_params(axis='x', labelsize=labelsize)
line3, = ax3.plot(px, py, '.-', color=color)
ax3.grid(which='both', axis='both', alpha=.4,linestyle='--')
ax3.set_title('y(t) vs x(t)', fontsize=fontsize)

#   adjust the subplots region to leave some space for the sliders and buttons
fig.subplots_adjust(left=0.1, bottom=0.195)


#   add 4 sliders for tweaking the parameters
#   define an axes area and draw a slider in it
axis_color = 'lightgoldenrodyellow'

y_slider_ax = fig.add_axes([0.15, 0.1, 0.65, 0.02], facecolor=axis_color)
y_slider = Slider(y_slider_ax, 'Launch Height', 0, 24.0, valinit=y0, valstep=0.5, valfmt="%2.0f  in")

v_slider_ax = fig.add_axes([0.15, 0.075, 0.65, 0.02], facecolor=axis_color)
v_slider = Slider(v_slider_ax, 'Launch Speed', 0, 700.0, valinit=v0, valstep=1, valfmt="%3.1f  in/s")

angle_slider_ax = fig.add_axes([0.15, 0.05, 0.65, 0.02], facecolor=axis_color)
angle_slider = Slider(angle_slider_ax, 'Launch Angle', 10, 55.0, valinit=angle, valstep=0.1, valfmt="%2.1f  deg")
   
ar_slider_ax  = fig.add_axes([0.15, 0.025, 0.65, 0.02], facecolor=axis_color)
ar_slider = Slider(ar_slider_ax, 'Air Res Coef', 0, 0.05, valinit=ar, valstep=0.001, valfmt="%1.3f  1/in")

#   add a button for rescaling the graphs
rescale_button_ax = fig.add_axes([0.90, 0.025, 0.075, 0.02])
rescale_button = Button(rescale_button_ax, 'Rescale', color=axis_color, hovercolor='0.975')

#   rescale all 3 graphs when the 'rescale' button is clicked
def rescale_button_on_clicked(mouse_event):
    ax1.relim()
    ax1.autoscale_view()
    ax1b.relim()
    ax1b.autoscale_view()

    ax2.relim()
    ax2.autoscale_view()
    ax2b.relim()
    ax2b.autoscale_view()

    ax3.relim()
    ax3.autoscale_view()
    
    #   redraw canvas
    fig.canvas.draw()


#   update all graphs
#   compute new velocities and positions
#   redraw the graphs
def update(val):
    
    global y0
    global v0
    global angle
    global ar
    
    y0 = y_slider.val
    v0 = v_slider.val
    angle = angle_slider.val
    ar = ar_slider.val

    #   compute new velocities and positions
    compute()

    #   update curve
    line1.set_data(pt, pvy)
    line1b.set_data(pt, py)
    line2.set_data(pt, pvx)
    line2b.set_data(pt, px)
    line3.set_data(px, py)

   #    redraw canvas
    fig.canvas.draw()

#   call update function on slider value change
y_slider.on_changed(update)
v_slider.on_changed(update)
ar_slider.on_changed(update)
angle_slider.on_changed(update)

#   call update function on the 'rescale' button click
rescale_button.on_clicked(rescale_button_on_clicked)

#   display
plt.show()