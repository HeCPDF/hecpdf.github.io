---
layout: page
icon: fas fa-archive
order: 4
title: 图库
---

<ul>
  {% for image_file in site.static_files %}
    {% if image_file.path contains '/images/' %}
      {% assign path_prefix = image_file.path | slice: 0, 8 %}
      {% if path_prefix == '/images/' %}
        <li>
          <a href="{{ image_file.path }}">{{ image_file.path }}</a>
        </li>
      {% endif %}
    {% endif %}
  {% endfor %}
</ul>
