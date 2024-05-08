# Puppet manfiesto to fix wordpress site `LAMP`


exec { 'replace'
	command  => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
	provider => 'shell'
}
