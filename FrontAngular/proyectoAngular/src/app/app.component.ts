import { Component } from '@angular/core';
import { RouterOutlet , Router} from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'proyectoAngular';

  constructor(private router:Router){}

  Listar(){
    this.router.navigate(["listar"])
  }
  Nuevo(){
    this.router.navigate(["add"])
  }
  Editar(){
    this.router.navigate(["edit"])
  }

}
