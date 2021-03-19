import warnings
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS, FITSFixedWarning
from astropy.visualization import make_lupton_rgb

warnings.filterwarnings("ignore", "'cdfix' made the change 'Success'", FITSFixedWarning)


def fetch_cutout(ra, dec, pixscale=2.35, layer="dr8"):
    url = f"http://legacysurvey.org/viewer/cutout.fits?ra={ra}&dec={dec}&layer={layer}&pixscale={pixscale}"
    fp = fits.open(url)
    header = fp[0].header.copy()
    data = fp[0].data.copy()
    del fp[0].data
    del fp[0]
    fp.close()
    return header, data


header, data = fetch_cutout(119.6821, 32.7381, pixscale=1)
wcs = WCS(header)[0]
image_rgb = make_lupton_rgb(data[2], data[1], data[0], stretch=0.1)  # indices 0,1,2 = grz

plt.subplots(subplot_kw={'projection': wcs}, figsize=(6, 6))
plt.imshow(image_rgb, origin='lower')
plt.show()