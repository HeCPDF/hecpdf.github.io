---
layout: page
icon: fas fa-archive
order: 5
---
//presets for html-like part
<style>
    .thumbnail {
        width: 150px; /* 缩略图的宽度 */
        height: 200px; /* 缩略图的高度 */
        object-fit: cover; /* 保持图片的比例 */
        border: none; /* 去掉边框 */
        padding: 0; /* 去掉填充 */
        margin: 5px; /* 添加一些间距 */
    }
    .row {
        display: flex;
        flex-wrap: wrap;
        align-items: left;
        justify-content: space-around;
    }
</style>

// content
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

## Collection: Xia Xin's Notebook (Destroyed Part)

<div class="row">
  {% for i in (1..6) %}
    <img src="/images/2023/11/23/S3G-notebook-PNGver/S3G-notebook-{{ i }}.png" alt="第{{ i }}页" class="thumbnail">
  {% endfor %}
</div>
