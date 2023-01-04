# [140-Eclipse](https://cssbattle.dev/play/140)

```html
<main>
  <div class='moon'>
    <div class='arc'></div>
  </div>
  <div class="mountain">
  </div>
</main>
<style>
  * {
    margin: 0;
    padding: 0;
  }
  main {
    width: 100vw;
    height: 100vh;
    background: #4F77FF;

  }
  .moon {
    position: fixed;
    top: 50px;
    left: calc(50vw - 40px);
    width: 80px;
    height: 80px;
    background: #FFFFFF;
    border-radius: 40px;
  }
  .moon .arc {
    position: absolute;
    top: 40px;
    width: 80px;
    height: 80px;
    background: #4F77FF;
    border-radius: 40px;
  }
  .mountain {
    position: fixed;
    bottom: 0px;
    left: calc(50vw - 162px);
    width: 0;
    height: 0;
    border-left: 162px solid transparent;
    border-right: 162px solid transparent;
    border-top: 162px solid transparent;
    border-bottom: 162px solid #1038BF;
  }
</style>

```
![](https://cssbattle.dev/targets/140.png)
