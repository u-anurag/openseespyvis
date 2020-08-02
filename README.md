# openseespyvis
A developmenet branch of OpenSeesPy Visualization commands. This can be used while waiting for the next release of OpenSeesPy.
It is advisable to use the latest release of OpenSeesPy (once released) for stable functions.

Install this package with,
```bash
pip install openseespyvis
```

To use this package, import the commands from **openseespyvis** instead of *openseespy.postprocessing*. For example,

```bash
# import openseespy.postprocessing.Get_Rendering as opsplt
import openseespyvis.Get_Rendering as opsplt
```

Now, use all the openseespy visualization commands. For example,

```bash
opsplt.plot_model()
```
