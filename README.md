# win10toast-pimped

>An easy-to-use Python library for displaying Windows 10 Toast Notifications. Improved version of [win10toast](https://pypi.org/project/win10toast/) and [win10toast-persist](https://pypi.org/project/win10toast-persist/) to include `callback_on_click` to run a function on notification click, for example to open a URL.

![](https://cloud.githubusercontent.com/assets/7101452/19763806/75f71ba4-9c5d-11e6-9f16-d0d4bf43e63e.png)

## Context

1: [Original module](https://github.com/jithurjacob/Windows-10-Toast-Notifications).

2: [Tweaked version with support for notifications that persist in the notification center](https://github.com/tnthieding/Windows-10-Toast-Notifications).

**This fork** is a pimped version of 2 ^ with `callback_on_click` that allows to run a function on notification click, for example to open a URL. 

## Installation

```
1) > pip install win10toast
2) > pip show win10toast
2) go to the location where win10toast was installed
3) replace original `__init__.py` with this version
```

<!-- ## Requirements

### Installation of pywin32
```
pypiwin32
setuptools
``` -->

## Example

```python
toaster = ToastNotifier() # initialize
toaster.show_toast(
    "Example two", # title
    "Click to open URL! >>", # message 
    icon_path=None, # icon_path 
    duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
    callback_on_click=open_url # click notification to run function 
    )
```

## Release History

- 0.1: Initial release.

## Versioning

Using [SemVer](http://semver.org/).

## Acknowledgements

- [win10toast](https://pypi.org/project/win10toast/)
- [win10toast-persist](https://pypi.org/project/win10toast-persist/)
- [click Windows 10 notification to open URL](https://stackoverflow.com/questions/63867448/interactive-notification-windows-10-using-python)