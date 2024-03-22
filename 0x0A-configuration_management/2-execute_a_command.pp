exec { 'kill killmenow':
  command  => 'pkill killmenow'
  provider => 'shell'
}
