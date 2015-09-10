# uWSGI Fastrouter

You'll need to add a line like this to your /etc/hosts:

    127.0.0.1    red.example.com blue.example.com green.example.com

You'll also need sudo to bind to port 80:

    sudo uwsgi --emperor ./vassals --master --vassal-set pythonpath=../