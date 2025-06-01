const express = require('express');
const fs = require('fs');
const app = express();
const port = 3000;

app.use(express.json());

const filePath = './click.txt';

// อ่านจำนวนคลิกจากไฟล์
function readCount() {
  try {
    const data = fs.readFileSync(filePath, 'utf8');
    return parseInt(data) || 0;
  } catch {
    return 0;
  }
}

// เขียนจำนวนคลิกลงไฟล์
function writeCount(count) {
  fs.writeFileSync(filePath, count.toString());
}

// API เพิ่มจำนวนคลิก
app.post('/click', (req, res) => {
  let count = readCount();
  count++;
  writeCount(count);
  res.json({ count });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
