#creats a file in /tmp
file { '/tmp/school':
  ensure => 'present',
  content => "I love Puppet\n",
  owner => 'www-data',
  group => 'www-data',
  mode => '0744'
}
