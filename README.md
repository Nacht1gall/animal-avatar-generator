<h2>Info</h2>
<p>Python implementation of <a href="https://github.com/roma-lukashik/animal-avatar-generator">Animal Avatar Generator</a></p>
<p>All credit goes to the original creator</p>

<h2>Installing</h2>
Install using `pip`:

```text
pip install animal-avatar
```

<h2>Usage</h2>

```python
from animal_avatar import Avatar
avatar = Avatar('your seed string')
svg = avatar.create_avatar()
```

<h3>Configuration options</h2>

|Name|Type|Description|Default|
|---|---|---|---|
|`size`|`int`|Avatar size in pixels|`150`|
|`avatar_colors`|`list`|Palette for avatar colors|`['#d7b89c', '#b18272','#ec8a90','#a1Ac88','#99c9bd','#50c8c6']`|
|`background_colors`|`list`|Palette for background colors|`['#fcf7d1', '#ece2e1','#e4e3cd','#c4ddd6','#b5f4bc']`|
|`blackout`|`bool`|Use blackout for right side of an avatar|`true`|
|`is_round`|`bool`|Use round or rectangle shape|`true`|

<p>Additionally you can install <a href="https://github.com/Kozea/CairoSVG">cairosvg</a> and convert the result to an image:</p>

```python
from cairosvg import svg2png
svg2png(bytestring=svg, write_to='test.png')
```
