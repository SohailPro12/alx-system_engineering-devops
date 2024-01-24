#install_nginx_web_server

class nginx_web_server {
  
  package { 'nginx':
    ensure => present,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
    ensure  => present,
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    content => "
server {
  listen 80;
  listen [::]:80;

  root /var/www/html;
  index index.html;

  server_name _;

  location /redirect_me {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
  }

  location / {
    try_files \$uri \$uri/ =404;
  }
}
",
    ensure  => present,
    require => Package['nginx'],
  }
}

include nginx_web_server

