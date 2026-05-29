$curveSvg = @'
    <div class="site-footer__curve" aria-hidden="true">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 400" preserveAspectRatio="none">
        <path fill="currentColor" d="M0,248 C240,268 420,312 640,292 C880,268 1080,168 1280,128 C1480,96 1720,112 1920,152 L1920,400 L0,400 Z"/>
      </svg>
    </div>
'@

function Get-Footer([string]$prefix, [switch]$Full) {
  $extra = if ($Full) {
@"
      <div>
        <h2>Visit</h2>
        <p>1828 ESE Loop 323, Suite LL-14<br>Tyler, TX 75701</p>
        <p>Mailing: P.O. Box 6134, Tyler, TX 75711</p>
      </div>
"@
  } else {
@"
      <div>
        <h2>Visit</h2>
        <p>1828 ESE Loop 323, Suite LL-14<br>Tyler, TX 75701</p>
      </div>
"@
  }

  $bottom = if ($Full) {
    '&copy; Tyler Deaf and Hard of Hearing Center &middot; Board preview mock-up'
  } else {
    '&copy; Tyler Deaf and Hard of Hearing Center'
  }

@"
  <footer class="site-footer">
$curveSvg
    <div class="site-footer__body">
      <div class="footer__inner">
        <div class="footer__logo">
          <img src="${prefix}assets/logo-white.png" alt="" width="392" height="245" class="footer__logo-img">
        </div>
        <div>
          <h2>Tyler Deaf and Hard of Hearing Center</h2>
          <p>501(c)(3) nonprofit &middot; Serving East Texas since 2012</p>
        </div>
$extra
        <div>
          <h2>Contact</h2>
          <p>VP: <a href="tel:+19032062210">(903) 206-2210</a></p>
          <p>Voice: <a href="tel:+19036176204">(903) 617-6204</a></p>
          <p><a href="mailto:coordinator@tdhhc.org">coordinator@tdhhc.org</a></p>
        </div>
      </div>
      <p class="footer__bottom">$bottom</p>
    </div>
  </footer>
"@
}

$siteRoot = Split-Path $PSScriptRoot -Parent

Get-ChildItem -Path $siteRoot -Recurse -Filter "*.html" | ForEach-Object {
  $depth = ($_.FullName.Substring($siteRoot.Length) -split '[\\/]').Count - 2
  $prefix = if ($depth -gt 0) { ("../" * $depth) } else { "" }
  $full = ($_.Name -eq "index.html" -and $_.DirectoryName -eq $siteRoot)

  $content = [System.IO.File]::ReadAllText($_.FullName)
  $footer = Get-Footer $prefix -Full:$full
  $content = [regex]::Replace($content, '(?s)<footer class="site-footer">.*?</footer>', $footer.TrimEnd())

  $content = $content -replace 'data-set-theme="v1">V1 Teal', 'data-set-theme="v1">V1 Slate'
  $content = $content -replace 'data-set-theme="v2">V2 Navy', 'data-set-theme="v2">V2 Navy'
  $content = $content -replace 'data-set-theme="v3">V3 Forest', 'data-set-theme="v3">V3 Wine'

  [System.IO.File]::WriteAllText($_.FullName, $content, [System.Text.UTF8Encoding]::new($false))
  Write-Host "Updated $($_.Name)"
}
