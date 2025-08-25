# Main game variables
surface   = None # The surface where all the graphics are drawn into
clock     = None
gui       = None # User interface 
scene     = None # The scene of the space
viewport  = None # Everything visible in the main area (excluding periferial viewports)

player     = None # The player Carrier instance
credits    = 10000

# World enities (destructable)
spaceships = []  # The list of ships owned by player
shipyards = [] # the least of shipyards available for player
docks     = [] # All the docks the player can dock into
aliens = [] # List of alien ships randomly spawning in space
asteroids = [] # List of randomly flying asteroids

cargos    = {}  # Cargos list used for iterations

# The modes that are elements of the gameplay
mode            = None # The current mode the game is in.
# The available game modes
fly_mode        = None
dock_mode       = None
shipyard_mode   = None

shipyard_menu = None # So to speak - menu available at the shipyard
cargo_panel = None # The cargo panel displayed when player hit's TAB or docks onto station
messenger   = None # The messenger displaying information about certain events that occur.
