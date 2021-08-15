# Kills a process called "Killmenow"

exec { 'kill_proces':

command => '/usr/bin/pkill killmenow',
provider => 'shell',
returns => [0,1],
}
