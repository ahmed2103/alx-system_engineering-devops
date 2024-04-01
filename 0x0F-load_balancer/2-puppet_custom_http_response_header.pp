# Puppet to add special header to web-server

exec { 'update':
  command => '/usr/bin/apt-get update',
}

# Install nginx
package { 'nginx':
  ensure => installed,
}

# Create directory and files
file { '/etc/nginx/html':
  ensure => directory,
}

file { '/etc/nginx/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/etc/nginx/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

# Configure nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
    listen 80;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /etc/nginx/html;
    index  index.html index.htm;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }
}',
  notify  => Service['nginx'],
}

# Restart nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}# Install nginx
package { 'nginx':
  ensure => installed,
}

# Create directory and files
file { '/etc/nginx/html':
  ensure => directory,
}

file { '/etc/nginx/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/etc/nginx/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

# Configure nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
    listen 80;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /etc/nginx/html;
    index  index.html index.htm;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }
}',
  notify  => Service['nginx'],
}

# Restart nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

