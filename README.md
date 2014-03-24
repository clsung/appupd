AppUpD
======

App Updater

Upload apk, and generate update.json

update.json
----
> [
>   {
>     "package_name": "str",
>     "download_link": "str",
>     "version": "str", //a.b.d
>     "activity_intent": "str",
>     "service_intent": "str",
>     "receiver_intent": "str" //Used to auto start activity/service/receiver after update
>   },
>   { ... },
> ]

Meta
----

* Code: `git clone git://github.com/clsung/appupd.git`
* Home: <http://github.com/clsung/appupd>
* Bugs: <http://github.com/clsung/appupd/issues>

Author
------

Cheng-Lung Sung :: clsung@gmail.com :: @clsung
