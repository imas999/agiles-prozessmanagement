import numpy as np
import matplotlib.pyplot as plt

# Parameter
frequenz = 10000  # 10 kHz
abtastrate = 500000  # 500 kHz (höhere Auflösung)
dauer = 0.01  # 10 ms (längere Dauer für bessere Frequenzauflösung)

# Zeitvektor
t = np.linspace(0, dauer, int(abtastrate * dauer), endpoint=False)

# Sinussignal generieren
signal = np.cos(2 * np.pi * frequenz * t)

# Diskrete Fourier Transformation (DFT) manuell berechnen
N = len(signal)
fft_werte = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(N, 1/abtastrate)

# Magnitude berechnen (vollständiges zweiseitiges Spektrum)
fft_magnitude = np.abs(fft_werte) / N

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Zeitbereich - diskretes Signal
# Zeige nur einen Ausschnitt für bessere Sichtbarkeit der Samples
anzeige_samples = 250  # Erste 250 Samples (entspricht 500 µs)
t_display = t[:anzeige_samples] * 1e6
signal_display = signal[:anzeige_samples]

# Zeichne kontinuierliche Linie (zum Vergleich, dünn und transparent)
ax1.plot(t_display, signal_display, 'b-', linewidth=0.5, alpha=0.3, label='Kontinuierlich (zur Orientierung)')
# Zeichne diskrete Samples als Stems
ax1.stem(t_display, signal_display, linefmt='b-', markerfmt='bo', basefmt=' ', label='Diskrete Samples')
ax1.set_xlabel('Zeit [µs]')
ax1.set_ylabel('Amplitude')
ax1.set_title(f'Diskretes Cosinussignal im Zeitbereich (f = {frequenz/1000} kHz, fs = {abtastrate/1000} kHz)')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 500)
ax1.axhline(y=0, color='k', linestyle='--', linewidth=0.5, alpha=0.5)
ax1.legend(loc='upper right')

# Frequenzbereich (vollständiges Spektrum anzeigen)
# Sortiere für bessere Darstellung: negative Frequenzen links, positive rechts
sorted_indices = np.argsort(fft_freq)
fft_freq_sorted = fft_freq[sorted_indices]
fft_magnitude_sorted = fft_magnitude[sorted_indices]

ax2.stem(fft_freq_sorted/1000, fft_magnitude_sorted, basefmt=' ', linefmt='b-', markerfmt='bo')
ax2.set_xlabel('Frequenz [kHz]')
ax2.set_ylabel('Magnitude')
ax2.set_title('Diskrete Fourier Transformation (DFT) - Vollständiges Spektrum')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(-20, 20)
ax2.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.5)

plt.tight_layout()
plt.savefig('sinus_10khz.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"Signal: Cosinus mit {frequenz/1000} kHz")
print(f"Abtastrate: {abtastrate/1000} kHz")
print(f"Anzahl Samples: {N}")
print(f"Frequenzauflösung: {abtastrate/N:.2f} Hz")
print(f"DFT verwendet: np.fft.fft (entspricht FFT-Algorithmus)")
print(f"Bild gespeichert als: sinus_10khz.png")
