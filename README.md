You must be logged in to use the cart functionality .

In admin panel categories section add these categories before adding images\
These all are case-sensitive\
  - menFashion\
 -  womenFashion\
  - kidFashion\
  - decor\
  - beauty\
  - electronics\
  - mobile\

# Install trivy

``` bash
curl -fsSL https://aquasecurity.github.io/trivy-repo/deb/public.key | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/trivy.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main" | \
sudo tee /etc/apt/sources.list.d/trivy.list

sudo apt update
sudo apt install trivy

```
# Install node
``` bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v
npm -v
```