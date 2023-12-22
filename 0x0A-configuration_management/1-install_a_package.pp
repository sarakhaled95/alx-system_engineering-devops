# install version 2.2.0 of flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'python':
  ensure   => '3.8.10',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
