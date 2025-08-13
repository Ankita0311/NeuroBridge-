# NeuroBridge

## Overview

NeuroBridge is an AI-powered mental health platform designed for early detection and support. The application serves as a landing page with email signup functionality to collect early access interest from potential users. The platform targets multiple demographics including youth, veterans, and indigenous communities, with plans to provide mental health screening and support services.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Framework
- **Flask Web Application**: Uses Flask as the core web framework for simplicity and rapid development
- **SQLAlchemy ORM**: Implements database operations through SQLAlchemy with declarative base model structure
- **Database Flexibility**: Configured to use SQLite for development (local file-based) with environment variable support for production databases

### Frontend Architecture
- **Server-Side Rendering**: Uses Flask's Jinja2 templating engine for HTML generation
- **Bootstrap 5**: Responsive CSS framework for consistent UI components and mobile compatibility
- **Progressive Enhancement**: JavaScript handles smooth scrolling, form validation, and interactive features
- **Custom CSS**: Calming color palette designed specifically for mental health applications

### Data Layer
- **EmailSignup Model**: Single table storing user registration data including email, name, user type (youth/veteran/indigenous/other), and timestamps
- **Email Validation**: Both client-side and server-side validation to ensure data quality
- **Duplicate Prevention**: Database constraints prevent duplicate email registrations

### Session Management
- **Flask Sessions**: Built-in session handling with configurable secret key
- **Flash Messages**: User feedback system for form submissions and validation errors

### Deployment Configuration
- **ProxyFix Middleware**: Handles reverse proxy headers for production deployment
- **Environment Variables**: Database URLs and session secrets configured through environment variables
- **Database Connection Pooling**: SQLAlchemy engine options for connection management and health checks

### Error Handling and Logging
- **Debug Logging**: Comprehensive logging for development and troubleshooting
- **Form Validation**: Multi-layer validation with user-friendly error messages
- **Graceful Failures**: Redirect patterns that maintain user experience during errors

## Recent Enhancements (August 2025)

### User Experience Improvements
- **Enhanced Animations**: Added fade-in animations for hero content and scroll-triggered element reveals
- **Trust Indicators**: Added HIPAA compliance, encryption, and clinical approval badges in signup section
- **Hero Statistics**: Implemented animated counters showing platform impact (85% earlier detection, 24/7 support, 1000+ lives touched)
- **Pulse Animation**: Added attention-grabbing pulse effect to primary CTA button
- **Real-time Form Validation**: Email input provides immediate visual feedback with green/red states

### Visual Polish
- **Enhanced Gradients**: Added radial gradient overlays to hero section for depth
- **Button Effects**: Implemented shimmer hover effects on all buttons
- **Navigation Enhancement**: Added underline animation to navigation links on hover
- **Improved Shadows**: Enhanced card shadows and hover states for better depth perception

### Technical Improvements
- **SEO Optimization**: Added comprehensive meta tags, Open Graph, Twitter Cards, and Schema.org markup
- **Accessibility**: Enhanced keyboard navigation, focus management, and screen reader support
- **Performance**: Optimized animations with reduced motion preferences and efficient JavaScript
- **Form UX**: Added loading states, better validation feedback, and auto-dismiss alerts

## External Dependencies

### Frontend Libraries
- **Bootstrap 5.3.0**: CSS framework and components via CDN
- **Font Awesome 6.4.0**: Icon library for UI elements
- **Google Fonts (Inter)**: Typography system for clean, readable text

### Python Packages
- **Flask**: Core web framework
- **Flask-SQLAlchemy**: Database ORM integration
- **Werkzeug**: WSGI utilities including ProxyFix middleware

### Database Options
- **SQLite**: Default development database (file-based)
- **Production Database**: Configurable through DATABASE_URL environment variable (supports PostgreSQL, MySQL, etc.)

### Development Tools
- **Python Logging**: Built-in logging system for debugging and monitoring
- **Regular Expressions**: Email validation pattern matching