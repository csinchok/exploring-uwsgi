# uWSGI Emperor Mode

Documentation: [http://uwsgi-docs.readthedocs.org/en/latest/Emperor.html](http://uwsgi-docs.readthedocs.org/en/latest/Emperor.html)

Emperor mode is a really great way to manage multiple apps at a time. On most distros, this is as simple as installing the package `uwsgi-emperor`, and adding some configs to your vassals directory.

To run the examples:

```bash
uwsgi --emperor ./vassals --master --vassal-set pythonpath=../
```

Now you can hit any of the apps on their respective ports:

  - red [http://127.0.0.1:8000](http://127.0.0.1:8000)
  - green [http://127.0.0.1:8001](http://127.0.0.1:8001)
  - blue [http://127.0.0.1:8002](http://127.0.0.1:8002)