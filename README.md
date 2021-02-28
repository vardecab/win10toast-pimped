# win10toast-click

>An easy-to-use Python library for displaying Windows 10 Toast Notifications. Improved version of [win10toast](https://pypi.org/project/win10toast/) and [win10toast-persist](https://pypi.org/project/win10toast-persist/) to include `callback_on_click` to run a function on notification click, for example to open a URL.

![](https://user-images.githubusercontent.com/6877391/109433448-9dc60d80-7a10-11eb-8c57-06760c2d638e.png)

## Context

1: [Original module](https://github.com/jithurjacob/Windows-10-Toast-Notifications).

2: [Tweaked version with support for notifications that persist in the notification center](https://github.com/tnthieding/Windows-10-Toast-Notifications).

**This fork** is an improved version of 2 ^ with `callback_on_click` that allows to run a function on notification click, for example to open a URL. 

## Installation

```bat
pip install win10toast-click
```

## Example

```python
# modules
import webbrowser
from win10toast_click import ToastNotifier 

# function 
page_url = 'http://example.com/'

def open_url():
    try: 
        webbrowser.open_new(page_url)
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')

# initialize 
toaster = ToastNotifier()

# showcase
toaster.show_toast(
    "Example two", # title
    "Click to open URL! >>", # message 
    icon_path=None, # 'icon_path' 
    duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
    callback_on_click=open_url # click notification to run function 
    )
```

## Release History

- 0.1.2: Prepared for distribution on Python Package Index (PyPI).
- 0.1.1: Renamed repo.
- 0.1: Initial release.

## Versioning

Using [SemVer](http://semver.org/).

## License

GNU General Public License v3.

## Acknowledgements
### Original modules
- [win10toast](https://pypi.org/project/win10toast/)
- [win10toast-persist](https://pypi.org/project/win10toast-persist/)
### Stack Overflow
- [click Windows 10 notification to open URL](https://stackoverflow.com/questions/63867448/interactive-notification-windows-10-using-python)
### Packaging & distribution 
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [`setuptools` Quickstart](https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html#including-data-files)
- [Data Files Support](https://setuptools.readthedocs.io/en/latest/userguide/datafiles.html)
- [Configuring setup() using setup.cfg files](https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html)
- [pypa packaging-problems](https://github.com/pypa/packaging-problems/issues)
### Icon
- [Flaticon / Freepik](https://www.flaticon.com/)