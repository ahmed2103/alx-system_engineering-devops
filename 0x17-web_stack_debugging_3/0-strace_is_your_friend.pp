# Puppet manfiesto to fix wordpress site `LAMP`

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
