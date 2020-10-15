# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 01:29:25 2019

@author: Amey
"""

from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

x_dirt = np.arange(0, 101, 1)
x_grease = np.arange(0, 101, 1)
x_time  = np.arange(0, 61, 1)

dirt_lo = fuzz.trimf(x_dirt, [0, 0, 50])
dirt_md=fuzz.trimf(x_dirt,[0,50,100])
dirt_hi = fuzz.trimf(x_dirt, [50, 100, 100])

grease_lo = fuzz.trimf(x_grease, [0, 0, 50])
grease_md = fuzz.trimf(x_grease, [0, 50, 100])
grease_hi = fuzz.trimf(x_grease, [50, 100, 100])

time_vs = fuzz.trimf(x_time, [0, 0, 10])
time_s = fuzz.trimf(x_time, [0, 10, 25])
time_m = fuzz.trimf(x_time, [10, 25, 40])
time_l = fuzz.trimf(x_time, [25, 40, 60])
time_vl = fuzz.trimf(x_time, [40, 60, 60])
fig, (ax, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax.plot(x_dirt, dirt_lo, 'b', linewidth=1.5, label='low')
ax.plot(x_dirt, dirt_md, 'g', linewidth=1.5, label='medium')
ax.plot(x_dirt, dirt_hi, 'r', linewidth=1.5, label='high')
ax.set_title('dirt')
ax.legend()

ax1.plot(x_grease, grease_lo, 'b', linewidth=1.5, label='low')
ax1.plot(x_grease, grease_md, 'g', linewidth=1.5, label='medium')
ax1.plot(x_grease, grease_hi, 'r', linewidth=1.5, label='high')
ax1.set_title('grease')
ax1.legend()

ax2.plot(x_time, time_vs, 'b', linewidth=1.5, label='very slow')
ax2.plot(x_time, time_s, 'g', linewidth=1.5, label='slow')
ax2.plot(x_time, time_m, 'r', linewidth=1.5, label='medium')
ax2.plot(x_time, time_l, 'b', linewidth=1.5, label='very slow')
ax2.plot(x_time, time_vl, 'g', linewidth=1.5, label='very slow')
ax2.set_title('Time')
ax2.legend()

for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

m,n = int(input("Enter dirt percentage : ")),int(input("Enter grease percentage : "))

dirt_level_lo = fuzz.interp_membership(x_dirt, dirt_lo, m)
dirt_level_md = fuzz.interp_membership(x_dirt, dirt_md, m)
dirt_level_hi = fuzz.interp_membership(x_dirt, dirt_hi, m)

print("membership function for dirt")
print('\u03bclo(%.f)'%m ,dirt_level_lo)
print('\u03bcmd(%.f)'%m ,dirt_level_md)
print('\u03bchi(%.f)'%m,dirt_level_hi)

grease_level_lo = fuzz.interp_membership(x_grease, grease_lo, n)
grease_level_md = fuzz.interp_membership(x_grease, grease_md, n)
grease_level_hi = fuzz.interp_membership(x_grease, grease_hi, n)
print("membership function for grease")
print('\u03bclo(%.f)'%n ,grease_level_lo)
print('\u03bcmd(%.f)'%n,grease_level_md)
print('\u03bchi(%.f)'%n ,grease_level_hi)

'''step 3 : rule base
        ng  mg  lg
        0   1   2
0   sd  vs  m   l
1   md  s   m   l
2   ld  m   l   vs'''

r1=np.fmin(dirt_level_lo,grease_level_lo);print(r1)
r2=np.fmin(dirt_level_lo,grease_level_md);print(r2)
r3=np.fmin(dirt_level_lo,grease_level_hi);print(r3)
r4=np.fmin(dirt_level_md,grease_level_lo);print(r4)
r5=np.fmin(dirt_level_md,grease_level_md);print(r5)
r6=np.fmin(dirt_level_md,grease_level_hi);print(r6)
r7=np.fmin(dirt_level_hi,grease_level_lo);print(r7)
r8=np.fmin(dirt_level_hi,grease_level_md);print(r8)
r9=np.fmin(dirt_level_hi,grease_level_hi);print(r9)

r1_a=np.fmin(r1,time_vs); print(r1_a)
r2_a=np.fmin(r2,time_m);print(r2_a)
r3_a=np.fmin(r3,time_l); print(r3_a)
r4_a=np.fmin(r4,time_s);print(r4_a)
r5_a=np.fmin(r5,time_m); print(r5_a)
r6_a=np.fmin(r6,time_l);print(r6_a)
r7_a=np.fmin(r7,time_m); print(r7_a)
r8_a=np.fmin(r8,time_l);print(r8_a)
r9_a=np.fmin(r9,time_vl); print(r9_a)

time0 = np.zeros_like(x_time)

fig, ax0 = plt.subplots(figsize=(8, 3))
ax0.fill_between(x_time, time0,r1_a, facecolor='b', alpha=0.7)
ax0.plot(x_time, time_vs, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_time, time0, r2_a, facecolor='g', alpha=0.7)
ax0.plot(x_time, time_m, 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(x_time, time0, r3_a, facecolor='r', alpha=0.7)
ax0.plot(x_time, time_l, 'r', linewidth=0.5, linestyle='--')

ax0.fill_between(x_time, time0,r4_a, facecolor='b', alpha=0.7)
ax0.plot(x_time, time_s, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_time, time0, r5_a, facecolor='g', alpha=0.7)
ax0.plot(x_time, time_m, 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(x_time, time0, r6_a, facecolor='r', alpha=0.7)
ax0.plot(x_time, time_l, 'r', linewidth=0.5, linestyle='--')

ax0.fill_between(x_time, time0,r7_a, facecolor='b', alpha=0.7)
ax0.plot(x_time, time_m, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_time, time0, r8_a, facecolor='g', alpha=0.7)
ax0.plot(x_time, time_l, 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(x_time, time0, r9_a, facecolor='r', alpha=0.7)
ax0.plot(x_time, time_vl, 'r', linewidth=0.5, linestyle='--')

ax0.set_title('Output membership activity')

fig, ax0 = plt.subplots(figsize=(8, 3))
ax0.fill_between(x_time, time0,r1_a, facecolor='b', alpha=0.7)
ax0.plot(x_time, time_vs, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_time, time0, r2_a, facecolor='g', alpha=0.7)
ax0.plot(x_time, time_m, 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(x_time, time0, r3_a, facecolor='r', alpha=0.7)
ax0.plot(x_time, time_l, 'r', linewidth=0.5, linestyle='--')

ax0.fill_between(x_time, time0,r4_a, facecolor='b', alpha=0.7)
ax0.plot(x_time, time_s, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_time, time0, r5_a, facecolor='g', alpha=0.7)
ax0.plot(x_time, time_m, 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(x_time, time0, r6_a, facecolor='r', alpha=0.7)
ax0.plot(x_time, time_l, 'r', linewidth=0.5, linestyle='--')

ax0.fill_between(x_time, time0,r7_a, facecolor='b', alpha=0.7)
ax0.plot(x_time, time_m, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_time, time0, r8_a, facecolor='g', alpha=0.7)
ax0.plot(x_time, time_l, 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(x_time, time0, r9_a, facecolor='r', alpha=0.7)
ax0.plot(x_time, time_vl, 'r', linewidth=0.5, linestyle='--')

ax0.set_title('Output membership activity')
aggregated = np.fmax(r9_a,np.fmax(r8_a,np.fmax(r7_a,np.fmax(r6_a,np.fmax(r5_a,np.fmax(r4_a,np.fmax(r3_a,np.fmax(r2,r1))))))))
print(aggregated)

time = fuzz.defuzz(x_time,aggregated, 'mom')
print(time)

time_activation = fuzz.interp_membership(x_time, aggregated, time)  # for plot
print(time_activation)

fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(x_time, time_vs, 'b', linewidth=0.5, linestyle='--', )
ax0.plot(x_time, time_s, 'g', linewidth=0.5, linestyle='--')
ax0.plot(x_time, time_m, 'r', linewidth=0.5, linestyle='--')
ax0.plot(x_time, time_vs, 'b', linewidth=0.5, linestyle='--', )
ax0.plot(x_time, time_l, 'g', linewidth=0.5, linestyle='--')
ax0.plot(x_time, time_vl, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(x_time, time0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([time, time], [0, time_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')

print("time needed",time)
