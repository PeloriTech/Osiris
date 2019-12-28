import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';

export interface UsbCameraDevice {
  name: string;
  path: string;

}

export interface Processors {
  name: string;
}

export interface Outputs {
  name: string;
}

@Component({
  selector: 'app-create-new-pipe',
  templateUrl: './create-new-pipe.component.html',
  styleUrls: ['./create-new-pipe.component.css']
})
export class CreateNewPipeComponent implements OnInit {

  firstFormGroup: FormGroup;
  secondFormGroup: FormGroup;
  thirdFormGroup: FormGroup;

  sources: string[] = ['rtsp', 'usb'];
  usbDevices: UsbCameraDevice[] = [{name: 'USB Camera 1', path: '/dev/video0'}, {
    name: 'USB Camera 2',
    path: '/dev/video1'
  }];

  processors: Processors[] = [{name:'YoloV3'}, {name: 'YoloV2'}, {name:'Sam Wheel Chair - BETA'}];

  outputs: Outputs[] = [{name:'JPEG Rotating Stream'}, {name:'Gstreamer TCPSERVERSINK'}];

  constructor(private formBuilder: FormBuilder) {
  }

  ngOnInit() {
    this.firstFormGroup = this.formBuilder.group({
      source_name: ['', Validators.required],
      source_type: '',
      usb_device: ''

    });
    this.secondFormGroup = this.formBuilder.group({
      processor: ['', Validators.required]
    });
    this.thirdFormGroup = this.formBuilder.group({
      output: ['', Validators.required]
    });
  }

}
