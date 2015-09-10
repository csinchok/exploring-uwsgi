# uWSGI Fastrouter

Documentation: [http://uwsgi-docs.readthedocs.org/en/latest/Fastrouter.html](http://uwsgi-docs.readthedocs.org/en/latest/Fastrouter.html)

You'll need to add a line like this to your /etc/hosts:

 ```
 127.0.0.1    red.example.com blue.example.com green.example.com
 ```

You'll (probably) also need sudo to bind to port 80:

```bash
sudo uwsgi --emperor ./vassals --master --vassal-set pythonpath=../
```

Now you'll be able to hit any of the apps via these URLS:

  - red [http://red.example.com](http://red.example.com)
  - green [http://red.example.com](http://green.example.com)
  - blue [http://red.example.com](http://blue.example.com)
