from importlib import reload
import mod_b


reload(mod_b)
print(mod_b.mod_c.x)

# this happen, because we imported script "mod_c" and now we can to access
# the objects of this sript

# after we changed mod_c we must reloab the imported mod_c
# that the changes are updated
