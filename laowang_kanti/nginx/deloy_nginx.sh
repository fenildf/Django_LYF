docker run -d  \
-v /home/liushuai/git/laowang_kanti/web:/var/laowangkanti/web  \
-v /home/liushuai/git/laowang_kanti/logs/nginx:/var/laowangkanti/logs/nginx/:ro  \
-v /home/liushuai/git/laowang_kanti/nginx/nginx.conf:/etc/nginx/nginx.conf:ro  \
-p 8989:8989  \
--name laowangkanti_nginx nginx
