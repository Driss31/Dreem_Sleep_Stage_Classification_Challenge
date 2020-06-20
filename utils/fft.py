import numpy as np

from scipy.fftpack import fft


def get_fft_values(y_values, t, n):
    """Returns two arrays, the first contains the frequency values, and the second the Fast Fourier Transform values"""
    f_values = np.linspace(0.0, 1.0 / (2.0 * t), n // 2)
    fft_values_ = fft(y_values)
    fft_values = 2.0 / n * np.abs(fft_values_[0 : n // 2])
    return f_values, fft_values


# t_n = 10
# N = 1000
# T = t_n / N
# f_s = 1 / T

# f_values, fft_values = get_fft_values(composite_y_value, T, N, f_s)
#
# plt.plot(f_values, fft_values, linestyle='-', color='blue')
# plt.xlabel('Frequency [Hz]', fontsize=16)
# plt.ylabel('Amplitude', fontsize=16)
# plt.title("Frequency domain of the signal", fontsize=16)
# plt.show()
