import {Component, Input, OnInit} from '@angular/core';
import {Block} from "../../model/block";

@Component({
  selector: 'app-block',
  templateUrl: './block.component.html',
  styleUrls: ['./block.component.css']
})
export class BlockComponent{
  @Input()
  block?: Block
}
