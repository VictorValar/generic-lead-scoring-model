Clear-Host
Write-Host "Deleting folders..."
Remove-Item -Recurse -Force build, dist, *.egg-info

Write-Host "Building dist..."
python setup.py sdist bdist_wheel

Write-Host "Upload to PyPI..."
twine upload dist/*

Write-Host "Done!"
