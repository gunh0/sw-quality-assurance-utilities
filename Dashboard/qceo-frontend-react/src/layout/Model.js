import React from 'react';
import ReactDOM from 'react-dom';

import Container from '@material-ui/core/Container';

const Modal = props => {
  return ReactDOM.createPortal(
    <Container>
      <div onClick={props.onDismiss} className='ui active dimmer'>
        <div onClick={e => e.stopPropagation()} className='ui active modal'>
          <div className='header'>{props.title}</div>
          <div className='content'>{props.content}</div>
          <div className='actions'>{props.actions}</div>
        </div>
      </div>
    </Container>,
    document.querySelector('#modal')
  );
};

export default Modal;
