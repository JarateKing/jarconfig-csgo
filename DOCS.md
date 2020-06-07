# Documentation

## Binds

Binds are functions that are intended to be bound to a key. For example, if you were to have a function like `jar_example` that is meant as a bind, you could use it like:

```
bind 1 "jar_example"
```

Which will do the `jar_example` function every time the `1` key is pressed.

### Movement

There are several binds that are intended to replace the basic movement binds. They are:

```
bind w "+jar_forward"
bind a "+jar_left"
bind s "+jar_back"
bind d "+jar_right"
bind space "+jar_jump"
bind ctrl "+jar_crouch"
```

They come with several options found in `settings.cfg` as well:

* `alias jar_on_movement ""` exists so that you can perform commands when you move. For example, `"r_cleardecals"` will remove all bullet holes / blood splatters when you move.
* `jar_mov_null=disable` lets you either enable or disable null-cancelling movement, where pressing `A` then `D` (while `A` is still held down) will make you move right rather than stand still.
* `jar_mov_cjump=disable` lets you either enable or disable crouchjumps, where you will crouch midair as you jump.

### Jumpthrow

The jumpthrow keybind is a simple:

```
+jar_jumpthrow
```

### Buyscript

There are many different keybinds that can be used for buyscript:

```
jar_buy_ak47
jar_buy_aug
jar_buy_awp
jar_buy_bizon
jar_buy_deagle
jar_buy_decoy
jar_buy_defuser
jar_buy_elite
jar_buy_famas
jar_buy_fiveseven
jar_buy_flashbang
jar_buy_g3sg1
jar_buy_galilar
jar_buy_hegrenade
jar_buy_incgrenade
jar_buy_m249
jar_buy_m4a1
jar_buy_mac10
jar_buy_mag7
jar_buy_molotov
jar_buy_mp7
jar_buy_mp9
jar_buy_negev
jar_buy_nova
jar_buy_p250
jar_buy_p90
jar_buy_revolver
jar_buy_sawedoff
jar_buy_scar20
jar_buy_sg556
jar_buy_smokegrenade
jar_buy_ssg08
jar_buy_taser
jar_buy_tec9
jar_buy_ump45
jar_buy_vest
jar_buy_vesthelm
jar_buy_xm1014
```

As well as various binds that can be used to attempt to buy two different things at once:

```
jar_buy_vesthelm+vest
jar_buy_ak47+m4a1
jar_buy_aug+sg556
jar_buy_famas+galilar
jar_buy_g3sg1+scar20
jar_buy_mac10+mp9
jar_buy_mag7+sawedoff
jar_buy_fiveseven+tec9
jar_buy_deagle+revolver
jar_buy_incgrenade+molotov
```

Each of these binds can be modified to automatically drop after buying, either throw a button you hold down that's bound to:

```
+jar_buydrop
```

Or a button that toggles whether or not to drop the weapon:

```
jar_buydrop_toggle
```
