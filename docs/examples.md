## Plot images from all channels

```python
from sm4file import Sm4
import matplotlib.pyplot as plt


sm4 = Sm4("path/to/sm4-file")

for channel in sm4:
    plt.imshow(channel.data)
    plt.title(f"{channel.label} - {channel.scan_direction}")
    plt.show()  # or plt.save()
```
  

## Plot all spectra, e.g. IV

```python
from sm4file import Sm4
import matplotlib.pyplot as plt


sm4 = Sm4("path/to/sm4-file")

for channel in sm4:
    for i in range(1, len(channel.data[0])):
        plt.plot(channel.data[:, 0], channel.data[:, i], label=f"{i}")
        plt.title(channel.label)
        plt.legend()

    plt.show()  # or plt.save()
```
