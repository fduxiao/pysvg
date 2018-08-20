from pysvg import *
from math import sqrt

MWIDTH = 400
D = 10
BASE = D/2
COUNT = MWIDTH / BASE
RADIUS = D * sqrt(2)
COLOR = "#11337C"

arm1 = MWIDTH / 4 - D / 2 - D
arm2 = arm1 - D
arm3 = arm2 - D

diamond = SVG(width=MWIDTH, height=MWIDTH)

# up
diamond.add_shape(Shape('path', d=f"""
    M {MWIDTH/2} 0 
    l {-arm2} {arm2}
    c {-D} {D} {0-D} {4*D-D} {0} {4*D}
    l {arm3} {arm3}
    l {-D/2} {D/2} {D} {D} {D/2} {-D/2}
    l {0} {-2*D} {-arm3} {-arm3}
    c {-D/2} {-D/2} {0-D/2} {-2*D+D/2} {0} {-2*D}
    l {arm3} {-arm3}
    Z
""", style=Style(fill=COLOR)))

diamond.add_shape(Shape('path', d=f"""
    M {MWIDTH/2} 0 
    l {arm2} {arm2}
    c {D} {D} {0+D} {4*D-D} {0} {4*D}
    l {-arm3} {arm3}
    l {D/2} {D/2} {-D} {D} {-D/2} {-D/2}
    l {0} {-2*D} {arm3} {-arm3}
    c {D/2} {-D/2} {0+D/2} {-2*D+D/2} {0} {-2*D}
    l {-arm3} {-arm3}
    Z
""", style=Style(fill=COLOR)))

# down
diamond.add_shape(Shape('path', d=f"""
    M {MWIDTH/2} {MWIDTH} 
    l {-arm2} {-arm2}
    c {-D} {-D} {0-D} {-4*D+D} {0} -{4*D}
    l {arm3} {-arm3}
    l {-D/2} {-D/2} {D} {-D} {D/2} {D/2}
    l {0} {2*D} {-arm3} {arm3}
    c {-D/2} {D/2} {0-D/2} {2*D-D/2} {0} {2*D}
    l {arm3} {arm3}
    Z
""", style=Style(fill=COLOR)))

diamond.add_shape(Shape('path', d=f"""
    M {MWIDTH/2} {MWIDTH} 
    l {arm2} {-arm2}
    c {D} {-D} {0+D} {-4*D+D} {0} -{4*D}
    l {-arm3} {-arm3}
    l {D/2} {-D/2} {-D} {-D} {-D/2} {D/2}
    l {0} {2*D} {arm3} {arm3}
    c {D/2} {D/2} {0+D/2} {2*D-D/2} {0} {2*D}
    l {-arm3} {arm3}
    Z
""", style=Style(fill=COLOR)))

# left
diamond.add_shape(Shape('path', d=f"""
    M 0 {MWIDTH/2} 
    l {arm2} {-arm2}
    c {D} {-D} {4*D-D} {0-D} {4*D} {0}
    l {arm3} {arm3}
    l {D/2} {-D/2} {D} {D} {-D/2} {D/2}
    l {-2*D} {0} {-arm3} {-arm3}
    c {-D/2} {-D/2} {-2*D+D/2} {0-D/2} {-2*D} {0}
    l {-arm3} {arm3}
    Z
""", style=Style(fill=COLOR)))

diamond.add_shape(Shape('path', d=f"""
    M 0 {MWIDTH/2} 
    l {arm2} {arm2}
    c {D} {D} {4*D-D} {0+D} {4*D} {0}
    l {arm3} {-arm3}
    l {D/2} {D/2} {D} {-D} {-D/2} {-D/2}
    l {-2*D} {0} {-arm3} {arm3}
    c {-D/2} {D/2} {-2*D+D/2} {0+D/2} {-2*D} {0}
    l {-arm3} {-arm3}
    Z
""", style=Style(fill=COLOR)))

# right
diamond.add_shape(Shape('path', d=f"""
    M {MWIDTH} {MWIDTH/2} 
    l {-arm2} {-arm2}
    c {-D} {-D} {-4*D+D} {0-D} {-4*D} {0}
    l {-arm3} {arm3}
    l {-D/2} {-D/2} {-D} {D} {D/2} {D/2}
    l {2*D} {0} {arm3} {-arm3}
    c {D/2} {-D/2} {2*D-D/2} {0-D/2} {2*D} {0}
    l {arm3} {arm3}
    Z
""", style=Style(fill=COLOR)))

diamond.add_shape(Shape('path', d=f"""
    M {MWIDTH} {MWIDTH/2} 
    l {-arm2} {arm2}
    c {-D} {D} {-4*D+D} {0+D} {-4*D} {0}
    l {-arm3} {-arm3}
    l {-D/2} {D/2} {-D} {-D} {D/2} {-D/2}
    l {2*D} {0} {arm3} {arm3}
    c {D/2} {D/2} {2*D-D/2} {0+D/2} {2*D} {0}
    l {arm3} {-arm3}
    Z
""", style=Style(fill=COLOR)))

# gaps between each two of the above
diamond.add_shape(Shape('path', d=f"""
    M {MWIDTH/2} 0
    l {0} {2*D}
    m {0} {2*arm2}
    l {0} {2*D}

    M {MWIDTH/2} {MWIDTH}
    l {0} {-2*D}
    m {0} {-2*arm2}
    l {0} {-2*D}
""", stroke=f"{COLOR}", fill="none"))

diamond.add_shape(Shape('path', d=f"""
    M 0 {MWIDTH/2}
    l {2*D} 0
    m {2*arm2} 0
    l {2*D} 0

    M {MWIDTH} {MWIDTH/2}
    l {-2*D} 0
    m {-2*arm2} 0
    l {-2*D} 0
""", stroke=f"{COLOR}", fill="none"))

diamond.add_shape(Shape('path', d=f"""
    M {MWIDTH/2} {MWIDTH/2}
    m {-D/2} {-D/2}
    l {-D} {-D}

    M {MWIDTH/2} {MWIDTH/2}
    m {D/2} {-D/2}
    l {D} {-D}

    M {MWIDTH/2} {MWIDTH/2}
    m {-D/2} {D/2}
    l {-D} {D}

    M {MWIDTH/2} {MWIDTH/2}
    m {D/2} {D/2}
    l {D} {D}
""", stroke=f"{COLOR}", fill="none"))

print(diamond)
