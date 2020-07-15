CREATE TABLE staff
(
   u_id INT PRIMARY KEY NOT NULL,
   staff_name TEXT NOT NULL,
   staff_age INT NOT NULL,
   staff_gender CHAR(10),
   staff_address CHAR(96)
);

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common