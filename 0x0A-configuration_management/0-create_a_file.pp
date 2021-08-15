# Creates a file called "holberton" in /tmp/
# With "I love Puppet" in there.
file {'/tmp/holberton':

mode => '0744',
owner => 'www-data',
group => 'www-data',
content => 'I love Puppet'
}
