$files = Get-ChildItem -Path (Join-Path $PSScriptRoot "..") -Recurse -Filter "*.html"
foreach ($f in $files) {
  $c = [System.IO.File]::ReadAllText($f.FullName)

  $c = $c -replace '501\(c\)\(3\) nonprofit [^<]+ Serving East Texas', '501(c)(3) nonprofit &middot; Serving East Texas'
  $c = $c -replace '(<p class="site-band__bottom">)[^<]*(Tyler Deaf and Hard of Hearing Center) [^<]*(Board preview)', '$1&copy; $2 &middot; $3'
  $c = $c -replace 'Board preview [^<]+ switch looks', 'Board preview &mdash; switch looks'
  $c = $c -replace 'organizations [^<]+ not individual clients [^<]+ request', 'organizations&#8212;not individual clients&#8212;request'

  [System.IO.File]::WriteAllText($f.FullName, $c, [System.Text.UTF8Encoding]::new($false))
  Write-Host "Fixed $($f.Name)"
}
