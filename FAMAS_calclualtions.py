import numpy as np
import matplotlib.pyplot as plt
import cmath

# parameter
x_ampl = 1
y_ampl = 1
# -----
# FAMAS can correct the gain by +/- 1.5%
x_gain = 1 + 0.0  # sine
y_gain = 1 + 0.0    # cosine
# offset of x,y axis
x_offset = 0.0    # sine
y_offset = 0.0      # cosine
# orthogonality error of x,y axis
xy_orth_err_deg = 0.5 # in deg
#-------------------------------------------------------
alpha_rad =  np.arange(0,200)/100*np.pi  # adapt for resolution changes
#-------------------------------------------------------
alpha_deg = alpha_rad * 180/np.pi

z_c_phase_rad = np.zeros(len(alpha_rad))

xy_orth_err_rad = xy_orth_err_deg * np.pi/180

z_c = np.sin(alpha_rad+xy_orth_err_rad) * x_ampl * x_gain + x_offset + 1j * (np.cos(alpha_rad) * y_ampl * y_gain + y_offset)

for i in range(len(z_c_phase_rad)):
    z_c_phase_rad[i] = np.arctan2(z_c[i].real,z_c[i].imag)

z_c_phase_deg = z_c_phase_rad*180/np.pi

# map angle to [0, 360]
z_c_phase_deg = (z_c_phase_deg + 360) % 360;
alpha_z_phase_diff_deg =  z_c_phase_deg - alpha_deg

max_err = np.max(alpha_z_phase_diff_deg)
min_err = np.min(alpha_z_phase_diff_deg)

# print
print("max error = {0:2.2f} deg; min error = {1:2.2f} deg ".format(max_err, min_err))


# plot
plt.figure()
plt.scatter(z_c.real, z_c.imag)

plt.ylabel('y')
plt.xlabel('x')
plt.axes().set_aspect('equal', 'datalim')
plt.grid()
plt.show()


plt.figure()
plt.plot(alpha_deg, alpha_z_phase_diff_deg, '.k')
plt.ylabel('corrected-ideal (deg)')
plt.xlabel('angle (deg)')
#plt.legend()
plt.grid()
plt.show()

