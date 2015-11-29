#include <Servo.h>

Servo servo;

void setup() {
  Serial.begin(9600);  // シリアルポートを9600 bps[ビット/秒]で初期化
  servo.attach(9);      // 制御信号を送る出力ピンの設定
  pinMode(0, OUTPUT);
}

void loop() {
  int deg=0;            // 初期の回転角
  int a_in = 0;
  int distance = 0;
  // 0-180度回転
  for (deg=0; deg<180; deg++) {
    a_in = analogRead(0);               // 距離センサの出力を取得
    distance = ((6762/(a_in-9))-4)*10;  // アナログ入力値を距離に変換
    Serial.println(String(deg) + "," + String(distance));
    delay(20);          // 20ms待機
  }
  // 180-0度回転
  for (deg=180; deg>0; deg--) {
    a_in = analogRead(0);         // 距離センサの出力を取得
    distance = (6762/(a_in-9))-4; // アナログ入力値を距離に変換
    Serial.println(String(deg) + "," + String(distance));
    delay(20);          // 20ms待機
  }
}