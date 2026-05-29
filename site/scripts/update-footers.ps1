$waveToBand = @'
  <div class="wave-divider" aria-hidden="true">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 80" preserveAspectRatio="none">
      <path d="M0,40L48,45.3C96,51,192,61,288,64C384,67,480,53,576,48C672,43,768,53,864,58.7C960,64,1056,64,1152,58.7C1248,53,1344,43,1392,37.3L1440,32V80H0Z" fill="var(--color-band)"/>
    </svg>
  </div>
'@

function Get-BandFooter([string]$assetPrefix) {
@"
$waveToBand
  <section class="site-band" aria-label="Tyler Deaf and Hard of Hearing Center">
    <div class="site-band__grid">
      <div class="logo">
        <img src="${assetPrefix}assets/logo.png" alt="" width="392" height="245">
      </div>
      <div>
        <h2>Tyler Deaf and Hard of Hearing Center</h2>
        <p>501(c)(3) nonprofit · Serving East Texas since 2012</p>
      </div>
      <div>
        <h2>Visit</h2>
        <p>1828 ESE Loop 323, Suite LL-14<br>Tyler, TX 75701</p>
        <p>Mailing: P.O. Box 6134, Tyler, TX 75711</p>
      </div>
      <div>
        <h2>Contact</h2>
        <p>VP: <a href="tel:+19032062210">(903) 206-2210</a></p>
        <p>Voice: <a href="tel:+19036176204">(903) 617-6204</a></p>
        <p><a href="mailto:coordinator@tdhhc.org">coordinator@tdhhc.org</a></p>
      </div>
    </div>
    <p class="site-band__bottom">© Tyler Deaf and Hard of Hearing Center · Board preview mock-up</p>
  </section>
"@
}

$waveToBg = @'
  <div class="wave-divider" aria-hidden="true">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 80" preserveAspectRatio="none">
      <path d="M0,40L48,45.3C96,51,192,61,288,64C384,67,480,53,576,48C672,43,768,53,864,58.7C960,64,1056,64,1152,58.7C1248,53,1344,43,1392,37.3L1440,32V80H0Z" fill="var(--color-bg)"/>
    </svg>
  </div>
'@

$siteRoot = Split-Path $PSScriptRoot -Parent

Get-ChildItem -Path $siteRoot -Recurse -Filter "*.html" | ForEach-Object {
  if ($_.Name -eq "index.html" -and $_.DirectoryName -eq $siteRoot) { return }

  $depth = ($_.FullName.Substring($siteRoot.Length) -split '[\\/]').Count - 2
  $prefix = if ($depth -gt 0) { ("../" * $depth) } else { "" }

  $content = Get-Content $_.FullName -Raw -Encoding UTF8
  $footer = Get-BandFooter $prefix
  $content = [regex]::Replace($content, '(?s)<footer class="site-footer">.*?</footer>', $footer.TrimEnd())

  # Page hero: move h1 + first lead out of main
  if ($content -match '(?s)(<main id="main" class="[^"]*">)\s*<h1>([^<]+)</h1>\s*<p class="lead">([^<]+)</p>') {
    $mainOpen = $Matches[1]
    $h1 = $Matches[2]
    $lead = $Matches[3]
    $heroBlock = @"
  <header class="page-hero">
    <div class="container">
      <h1>$h1</h1>
      <p class="lead">$lead</p>
    </div>
  </header>
$waveToBg
$mainOpen

"@
    $content = [regex]::Replace($content, '(?s)<main id="main" class="[^"]*">\s*<h1>[^<]+</h1>\s*<p class="lead">[^<]+</p>\s*', $heroBlock, 1)
  }

  [System.IO.File]::WriteAllText($_.FullName, $content, [System.Text.UTF8Encoding]::new($false))
  Write-Host "Updated $($_.FullName)"
}
