#!/usr/bin/pup
# install version 2.2.0 of flask

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
