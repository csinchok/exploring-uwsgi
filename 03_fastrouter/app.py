def red(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"""<html><head><title>RED</title><style type="text/css">body {background-color:red;color: white;}</style></head><body><pre>
RRRRRRRRRRRRRRRRR   EEEEEEEEEEEEEEEEEEEEEEDDDDDDDDDDDDD        
R::::::::::::::::R  E::::::::::::::::::::ED::::::::::::DDD     
R::::::RRRRRR:::::R E::::::::::::::::::::ED:::::::::::::::DD   
RR:::::R     R:::::REE::::::EEEEEEEEE::::EDDD:::::DDDDD:::::D  
  R::::R     R:::::R  E:::::E       EEEEEE  D:::::D    D:::::D 
  R::::R     R:::::R  E:::::E               D:::::D     D:::::D
  R::::RRRRRR:::::R   E::::::EEEEEEEEEE     D:::::D     D:::::D
  R:::::::::::::RR    E:::::::::::::::E     D:::::D     D:::::D
  R::::RRRRRR:::::R   E:::::::::::::::E     D:::::D     D:::::D
  R::::R     R:::::R  E::::::EEEEEEEEEE     D:::::D     D:::::D
  R::::R     R:::::R  E:::::E               D:::::D     D:::::D
  R::::R     R:::::R  E:::::E       EEEEEE  D:::::D    D:::::D 
RR:::::R     R:::::REE::::::EEEEEEEE:::::EDDD:::::DDDDD:::::D  
R::::::R     R:::::RE::::::::::::::::::::ED:::::::::::::::DD   
R::::::R     R:::::RE::::::::::::::::::::ED::::::::::::DDD     
RRRRRRRR     RRRRRRREEEEEEEEEEEEEEEEEEEEEEDDDDDDDDDDDDD
</pre></body></html>"""]


def green(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"""<html><head><title>GREEN</title><style type="text/css">body {background-color:green;color: white;}</style></head><body><pre>
        GGGGGGGGGGGGGRRRRRRRRRRRRRRRRR   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEENNNNNNNN        NNNNNNNN
     GGG::::::::::::GR::::::::::::::::R  E::::::::::::::::::::EE::::::::::::::::::::EN:::::::N       N::::::N
   GG:::::::::::::::GR::::::RRRRRR:::::R E::::::::::::::::::::EE::::::::::::::::::::EN::::::::N      N::::::N
  G:::::GGGGGGGG::::GRR:::::R     R:::::REE::::::EEEEEEEEE::::EEE::::::EEEEEEEEE::::EN:::::::::N     N::::::N
 G:::::G       GGGGGG  R::::R     R:::::R  E:::::E       EEEEEE  E:::::E       EEEEEEN::::::::::N    N::::::N
G:::::G                R::::R     R:::::R  E:::::E               E:::::E             N:::::::::::N   N::::::N
G:::::G                R::::RRRRRR:::::R   E::::::EEEEEEEEEE     E::::::EEEEEEEEEE   N:::::::N::::N  N::::::N
G:::::G    GGGGGGGGGG  R:::::::::::::RR    E:::::::::::::::E     E:::::::::::::::E   N::::::N N::::N N::::::N
G:::::G    G::::::::G  R::::RRRRRR:::::R   E:::::::::::::::E     E:::::::::::::::E   N::::::N  N::::N:::::::N
G:::::G    GGGGG::::G  R::::R     R:::::R  E::::::EEEEEEEEEE     E::::::EEEEEEEEEE   N::::::N   N:::::::::::N
G:::::G        G::::G  R::::R     R:::::R  E:::::E               E:::::E             N::::::N    N::::::::::N
 G:::::G       G::::G  R::::R     R:::::R  E:::::E       EEEEEE  E:::::E       EEEEEEN::::::N     N:::::::::N
  G:::::GGGGGGGG::::GRR:::::R     R:::::REE::::::EEEEEEEE:::::EEE::::::EEEEEEEE:::::EN::::::N      N::::::::N
   GG:::::::::::::::GR::::::R     R:::::RE::::::::::::::::::::EE::::::::::::::::::::EN::::::N       N:::::::N
     GGG::::::GGG:::GR::::::R     R:::::RE::::::::::::::::::::EE::::::::::::::::::::EN::::::N        N::::::N
        GGGGGG   GGGGRRRRRRRR     RRRRRRREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEENNNNNNNN         NNNNNNN                                                                         
</pre>
    </body>
    </html>"""]


def blue(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b'''<html><head><title>BLUE</title><style type="text/css">body {background-color:blue;color: white;}</style></head><body><pre>
BBBBBBBBBBBBBBBBB   LLLLLLLLLLL            UUUUUUUU     UUUUUUUUEEEEEEEEEEEEEEEEEEEEEE
B::::::::::::::::B  L:::::::::L            U::::::U     U::::::UE::::::::::::::::::::E
B::::::BBBBBB:::::B L:::::::::L            U::::::U     U::::::UE::::::::::::::::::::E
BB:::::B     B:::::BLL:::::::LL            UU:::::U     U:::::UUEE::::::EEEEEEEEE::::E
  B::::B     B:::::B  L:::::L               U:::::U     U:::::U   E:::::E       EEEEEE
  B::::B     B:::::B  L:::::L               U:::::D     D:::::U   E:::::E             
  B::::BBBBBB:::::B   L:::::L               U:::::D     D:::::U   E::::::EEEEEEEEEE   
  B:::::::::::::BB    L:::::L               U:::::D     D:::::U   E:::::::::::::::E   
  B::::BBBBBB:::::B   L:::::L               U:::::D     D:::::U   E:::::::::::::::E   
  B::::B     B:::::B  L:::::L               U:::::D     D:::::U   E::::::EEEEEEEEEE   
  B::::B     B:::::B  L:::::L               U:::::D     D:::::U   E:::::E             
  B::::B     B:::::B  L:::::L         LLLLLLU::::::U   U::::::U   E:::::E       EEEEEE
BB:::::BBBBBB::::::BLL:::::::LLLLLLLLL:::::LU:::::::UUU:::::::U EE::::::EEEEEEEE:::::E
B:::::::::::::::::B L::::::::::::::::::::::L UU:::::::::::::UU  E::::::::::::::::::::E
B::::::::::::::::B  L::::::::::::::::::::::L   UU:::::::::UU    E::::::::::::::::::::E
BBBBBBBBBBBBBBBBB   LLLLLLLLLLLLLLLLLLLLLLLL     UUUUUUUUU      EEEEEEEEEEEEEEEEEEEEEE
</pre>
    </body>
    </html>''']
