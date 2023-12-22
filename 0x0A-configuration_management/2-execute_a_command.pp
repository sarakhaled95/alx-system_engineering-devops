#kill process killmnow

exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
