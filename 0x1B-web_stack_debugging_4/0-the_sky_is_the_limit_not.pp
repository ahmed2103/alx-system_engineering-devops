#Puppet manifesto to fix failure with high amount of requests

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/15/4096/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
