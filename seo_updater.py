import os
import re
import glob

directory = r'c:\seminarkitsemarang.web.id'
html_files = glob.glob(os.path.join(directory, '*.html'))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if <!-- Vendor CSS Files --> is not present
    if '<!-- Vendor CSS Files -->' not in content:
        print(f"Skipping {file_path} - missing vendor css anchor")
        continue

    # Extract current title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    original_title = title_match.group(1) if title_match else "Seminar Kit Semarang"
    
    # Upgrade title if not already containing the suffix
    new_title = original_title
    if "Souvenir Kantor" not in original_title and "SeminarKit" not in original_title:
        if "Seminar Kit Semarang" in original_title:
            new_title = original_title + " | Souvenir Kantor Custom"
        else:
            new_title = original_title + " | SeminarKit Semarang, Souvenir Kantor Custom"

    filename = os.path.basename(file_path)
    if filename == "index.html":
        filename = "" # Canonical URL for root

    new_head_block = f"""<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{new_title}</title>
  
  <!-- SEO & AEO (Answer Engine Optimization) -->
  <meta name="description" content="Pusat seminar kit semarang, souvenir kantor semarang, dan seminarkit custom semarang. Temukan tas seminar, tumbler murah, pulpen, notes, dan merchandise event terbaik dengan harga pabrik. Hubungi kami untuk penawaran spesial!">
  <meta name="keywords" content="seminarkit semarang, souvenir kantor semarang, seminarkit custom semarang, tas seminar semarang, tumbler custom semarang, paket seminar murah, pabrik tas seminar, merchandise event semarang">
  
  <!-- PageSpeed Preconnects -->
  <link rel="dns-prefetch" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

  <!-- Canonical -->
  <link rel="canonical" href="https://seminarkitsemarang.web.id/{filename}" />

  <!-- OpenGraph / GEO & Social Media Sharing -->
  <meta property="og:title" content="{new_title}" />
  <meta property="og:description" content="Pusat seminar kit semarang, souvenir kantor semarang, dan seminarkit custom semarang. Temukan berbagai merchandise custom dengan harga terbaik." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://seminarkitsemarang.web.id/{filename}" />
  <meta property="og:image" content="https://seminarkitsemarang.web.id/assets/img/logo.webp" />
  <meta property="og:site_name" content="Seminar Kit Semarang" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{new_title}">
  <meta name="twitter:description" content="Pusat seminar kit semarang, souvenir kantor semarang, dan seminarkit custom semarang. Temukan berbagai merchandise custom dengan harga terbaik.">
  <meta name="twitter:image" content="https://seminarkitsemarang.web.id/assets/img/logo.webp">

  <!-- Favicons -->
  <link rel="icon" href="assets/img/favicon.webp" type="image/webp">
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
  <meta name="theme-color" content="#ffffff">

  <!-- Schema Markup (JSON-LD) for AEO & GEO -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Organization",
        "@id": "https://seminarkitsemarang.web.id/#organization",
        "name": "SeminarKit Semarang",
        "url": "https://seminarkitsemarang.web.id",
        "logo": "https://seminarkitsemarang.web.id/assets/img/logo.webp",
        "contactPoint": {{
          "@type": "ContactPoint",
          "telephone": "+6288989643555",
          "contactType": "customer service",
          "areaServed": "ID",
          "availableLanguage": "Indonesian"
        }}
      }},
      {{
        "@type": "WebSite",
        "@id": "https://seminarkitsemarang.web.id/#website",
        "url": "https://seminarkitsemarang.web.id/",
        "name": "Seminar Kit Semarang - Souvenir Kantor Custom",
        "publisher": {{"@id": "https://seminarkitsemarang.web.id/#organization"}}
      }},
      {{
        "@type": "LocalBusiness",
        "name": "Seminar Kit Semarang",
        "image": "https://seminarkitsemarang.web.id/assets/img/logo.webp",
        "url": "https://seminarkitsemarang.web.id/",
        "telephone": "+6288989643555",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "Semarang",
          "addressRegion": "Jawa Tengah",
          "addressCountry": "ID"
        }},
        "priceRange": "$$"
      }}
    ]
  }}
  </script>

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">

  """

    # Use regex to replace everything from <head> to <!-- Vendor CSS Files -->
    pattern = re.compile(r'<head>.*?(?=<!-- Vendor CSS Files -->)', re.IGNORECASE | re.DOTALL)
    
    new_content, count = pattern.subn(new_head_block, content, count=1)
    
    if count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Failed to find match for {file_path}")

print("SEO update completed.")
