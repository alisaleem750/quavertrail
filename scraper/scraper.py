from ContentProcessor import ContentProcessor

content_processor = ContentProcessor()
guardian_articles = content_processor.extract_content('https://www.theguardian.com/uk', '<a href="(.+?)" class="u-faux-block-link__overlay js-headline-text" data-link-name="article" tabindex="-1">')
print guardian_articles






